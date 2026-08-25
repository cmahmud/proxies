# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 419
- HTTP: 91 alive / 62 gold
- HTTPS: 78 alive / 20 gold
- SOCKS4: 182 alive / 164 gold
- SOCKS5: 192 alive / 173 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36128
- Ever gold: 1268

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
