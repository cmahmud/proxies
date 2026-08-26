# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 400
- HTTP: 92 alive / 59 gold
- HTTPS: 97 alive / 14 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 189 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39269
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
