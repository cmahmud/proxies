# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 400
- HTTP: 111 alive / 67 gold
- HTTPS: 55 alive / 17 gold
- SOCKS4: 167 alive / 155 gold
- SOCKS5: 187 alive / 161 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38940
- Ever gold: 1294

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
