# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 372
- HTTP: 95 alive / 56 gold
- HTTPS: 36 alive / 11 gold
- SOCKS4: 163 alive / 151 gold
- SOCKS5: 183 alive / 154 gold

## Historical pool

- Discovered: 174123
- Ever alive: 33058
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
