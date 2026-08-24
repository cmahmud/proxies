# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 389
- HTTP: 93 alive / 52 gold
- HTTPS: 42 alive / 12 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 180270
- Ever alive: 33550
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
