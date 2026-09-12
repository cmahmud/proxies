# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 434
- HTTP: 109 alive / 81 gold
- HTTPS: 47 alive / 30 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 178 alive / 164 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49445
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
