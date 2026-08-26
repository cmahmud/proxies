# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 419
- HTTP: 103 alive / 70 gold
- HTTPS: 83 alive / 20 gold
- SOCKS4: 179 alive / 163 gold
- SOCKS5: 186 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37952
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
