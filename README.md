# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 413
- HTTP: 94 alive / 71 gold
- HTTPS: 113 alive / 20 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 178 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41989
- Ever gold: 1347

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
