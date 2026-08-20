# SyndProxy private pool

## Current pool

- Alive now: 760
- Gold now: 388
- HTTP: 163 alive / 70 gold
- HTTPS: 170 alive / 18 gold
- SOCKS4: 197 alive / 144 gold
- SOCKS5: 230 alive / 156 gold

## Historical pool

- Discovered: 145577
- Ever alive: 25554
- Ever gold: 1063

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
