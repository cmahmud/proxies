# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 406
- HTTP: 93 alive / 58 gold
- HTTPS: 104 alive / 20 gold
- SOCKS4: 183 alive / 164 gold
- SOCKS5: 193 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41506
- Ever gold: 1336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
