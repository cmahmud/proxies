# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 414
- HTTP: 106 alive / 67 gold
- HTTPS: 75 alive / 19 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 193 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38024
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
