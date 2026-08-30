# SyndProxy validated proxy pool

## Current pool

- Alive now: 659
- Gold now: 481
- HTTP: 163 alive / 102 gold
- HTTPS: 129 alive / 42 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 198 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44973
- Ever gold: 1421

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
