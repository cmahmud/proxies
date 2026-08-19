# SyndProxy private pool

## Current pool

- Alive now: 1150
- Gold now: 547
- HTTP: 417 alive / 190 gold
- HTTPS: 305 alive / 84 gold
- SOCKS4: 219 alive / 130 gold
- SOCKS5: 209 alive / 143 gold

## Historical pool

- Discovered: 127340
- Ever alive: 19826
- Ever gold: 801

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
