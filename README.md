# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 381
- HTTP: 95 alive / 54 gold
- HTTPS: 42 alive / 10 gold
- SOCKS4: 172 alive / 154 gold
- SOCKS5: 186 alive / 163 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33428
- Ever gold: 1237

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
