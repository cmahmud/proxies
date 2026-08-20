# SyndProxy private pool

## Current pool

- Alive now: 738
- Gold now: 384
- HTTP: 163 alive / 68 gold
- HTTPS: 148 alive / 18 gold
- SOCKS4: 191 alive / 144 gold
- SOCKS5: 236 alive / 154 gold

## Historical pool

- Discovered: 145577
- Ever alive: 25557
- Ever gold: 1064

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
