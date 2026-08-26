# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 402
- HTTP: 102 alive / 61 gold
- HTTPS: 76 alive / 17 gold
- SOCKS4: 163 alive / 157 gold
- SOCKS5: 186 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38629
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
