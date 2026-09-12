# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 459
- HTTP: 117 alive / 90 gold
- HTTPS: 51 alive / 32 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 194 alive / 175 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49428
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
