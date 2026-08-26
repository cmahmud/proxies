# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 403
- HTTP: 103 alive / 60 gold
- HTTPS: 84 alive / 16 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 189 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39029
- Ever gold: 1296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
