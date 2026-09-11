# SyndProxy validated proxy pool

## Current pool

- Alive now: 459
- Gold now: 409
- HTTP: 81 alive / 64 gold
- HTTPS: 40 alive / 20 gold
- SOCKS4: 163 alive / 156 gold
- SOCKS5: 175 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48835
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
