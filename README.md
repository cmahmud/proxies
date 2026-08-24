# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 385
- HTTP: 105 alive / 47 gold
- HTTPS: 61 alive / 14 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 183 alive / 165 gold

## Historical pool

- Discovered: 180329
- Ever alive: 33571
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
