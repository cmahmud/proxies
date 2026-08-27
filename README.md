# SyndProxy validated proxy pool

## Current pool

- Alive now: 638
- Gold now: 437
- HTTP: 122 alive / 88 gold
- HTTPS: 127 alive / 20 gold
- SOCKS4: 189 alive / 160 gold
- SOCKS5: 200 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42211
- Ever gold: 1354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
