# SyndProxy private pool

## Current pool

- Alive now: 1219
- Gold now: 533
- HTTP: 448 alive / 186 gold
- HTTPS: 336 alive / 59 gold
- SOCKS4: 198 alive / 123 gold
- SOCKS5: 237 alive / 165 gold

## Historical pool

- Discovered: 125671
- Ever alive: 19662
- Ever gold: 775

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
