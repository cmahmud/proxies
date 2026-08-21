# SyndProxy private pool

## Current pool

- Alive now: 1013
- Gold now: 433
- HTTP: 330 alive / 99 gold
- HTTPS: 233 alive / 27 gold
- SOCKS4: 190 alive / 144 gold
- SOCKS5: 260 alive / 163 gold

## Historical pool

- Discovered: 153744
- Ever alive: 28758
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
