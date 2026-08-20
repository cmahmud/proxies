# SyndProxy private pool

## Current pool

- Alive now: 659
- Gold now: 377
- HTTP: 164 alive / 67 gold
- HTTPS: 104 alive / 21 gold
- SOCKS4: 186 alive / 136 gold
- SOCKS5: 205 alive / 153 gold

## Historical pool

- Discovered: 145577
- Ever alive: 25570
- Ever gold: 1066

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
