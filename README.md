# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 406
- HTTP: 109 alive / 64 gold
- HTTPS: 75 alive / 17 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 190 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38664
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
