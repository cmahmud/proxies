# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 418
- HTTP: 109 alive / 77 gold
- HTTPS: 41 alive / 19 gold
- SOCKS4: 176 alive / 158 gold
- SOCKS5: 176 alive / 164 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49459
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
