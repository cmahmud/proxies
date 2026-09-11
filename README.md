# SyndProxy validated proxy pool

## Current pool

- Alive now: 463
- Gold now: 410
- HTTP: 81 alive / 64 gold
- HTTPS: 44 alive / 21 gold
- SOCKS4: 163 alive / 156 gold
- SOCKS5: 175 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48837
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
