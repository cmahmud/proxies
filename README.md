# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 405
- HTTP: 98 alive / 61 gold
- HTTPS: 94 alive / 12 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 199 alive / 171 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38247
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
