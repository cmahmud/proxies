# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 405
- HTTP: 106 alive / 65 gold
- HTTPS: 64 alive / 18 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 196 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38695
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
