# SyndProxy private pool

## Current pool

- Alive now: 1628
- Gold now: 602
- HTTP: 630 alive / 213 gold
- HTTPS: 548 alive / 111 gold
- SOCKS4: 206 alive / 134 gold
- SOCKS5: 244 alive / 144 gold

## Historical pool

- Discovered: 141137
- Ever alive: 23844
- Ever gold: 962

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
