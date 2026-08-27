# SyndProxy validated proxy pool

## Current pool

- Alive now: 607
- Gold now: 414
- HTTP: 118 alive / 69 gold
- HTTPS: 129 alive / 16 gold
- SOCKS4: 173 alive / 164 gold
- SOCKS5: 187 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41385
- Ever gold: 1327

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
