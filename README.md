# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 400
- HTTP: 97 alive / 59 gold
- HTTPS: 72 alive / 15 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 176 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39068
- Ever gold: 1296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
