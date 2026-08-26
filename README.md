# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 412
- HTTP: 96 alive / 67 gold
- HTTPS: 68 alive / 19 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 184 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38613
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
