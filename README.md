# SyndProxy validated proxy pool

## Current pool

- Alive now: 581
- Gold now: 437
- HTTP: 135 alive / 83 gold
- HTTPS: 88 alive / 22 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 189 alive / 171 gold

## Historical pool

- Discovered: 181494
- Ever alive: 33983
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
