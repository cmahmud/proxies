# SyndProxy private pool

## Current pool

- Alive now: 1018
- Gold now: 337
- HTTP: 371 alive / 45 gold
- HTTPS: 193 alive / 9 gold
- SOCKS4: 224 alive / 143 gold
- SOCKS5: 230 alive / 140 gold

## Historical pool

- Discovered: 107060
- Ever alive: 14634
- Ever gold: 466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
