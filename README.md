# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 416
- HTTP: 107 alive / 69 gold
- HTTPS: 74 alive / 19 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 192 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38023
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
