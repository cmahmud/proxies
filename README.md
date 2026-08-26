# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 398
- HTTP: 91 alive / 54 gold
- HTTPS: 83 alive / 15 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 181 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39143
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
