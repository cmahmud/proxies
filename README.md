# SyndProxy validated proxy pool

## Current pool

- Alive now: 638
- Gold now: 454
- HTTP: 134 alive / 87 gold
- HTTPS: 144 alive / 33 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 187 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46849
- Ever gold: 1452

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
