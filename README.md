# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 405
- HTTP: 93 alive / 63 gold
- HTTPS: 75 alive / 18 gold
- SOCKS4: 163 alive / 157 gold
- SOCKS5: 187 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38629
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
