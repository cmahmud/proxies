# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 394
- HTTP: 112 alive / 68 gold
- HTTPS: 54 alive / 15 gold
- SOCKS4: 164 alive / 151 gold
- SOCKS5: 190 alive / 160 gold

## Historical pool

- Discovered: 175447
- Ever alive: 33162
- Ever gold: 1228

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
