# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 392
- HTTP: 93 alive / 58 gold
- HTTPS: 32 alive / 13 gold
- SOCKS4: 179 alive / 158 gold
- SOCKS5: 191 alive / 163 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33341
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
