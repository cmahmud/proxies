# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 404
- HTTP: 97 alive / 58 gold
- HTTPS: 102 alive / 20 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 182 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43019
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
