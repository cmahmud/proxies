# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 480
- HTTP: 148 alive / 100 gold
- HTTPS: 122 alive / 42 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 196 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44946
- Ever gold: 1420

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
