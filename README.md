# SyndProxy validated proxy pool

## Current pool

- Alive now: 595
- Gold now: 451
- HTTP: 148 alive / 92 gold
- HTTPS: 86 alive / 35 gold
- SOCKS4: 163 alive / 158 gold
- SOCKS5: 198 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44184
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
