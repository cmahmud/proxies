# SyndProxy private pool

## Current pool

- Alive now: 1032
- Gold now: 501
- HTTP: 340 alive / 141 gold
- HTTPS: 247 alive / 80 gold
- SOCKS4: 235 alive / 148 gold
- SOCKS5: 210 alive / 132 gold

## Historical pool

- Discovered: 119697
- Ever alive: 17905
- Ever gold: 705

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
