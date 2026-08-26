# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 402
- HTTP: 104 alive / 59 gold
- HTTPS: 83 alive / 16 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39028
- Ever gold: 1296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
