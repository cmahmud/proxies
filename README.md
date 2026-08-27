# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 406
- HTTP: 94 alive / 58 gold
- HTTPS: 101 alive / 20 gold
- SOCKS4: 183 alive / 164 gold
- SOCKS5: 192 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41507
- Ever gold: 1336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
