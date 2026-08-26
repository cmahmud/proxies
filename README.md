# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 410
- HTTP: 101 alive / 61 gold
- HTTPS: 88 alive / 16 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 202 alive / 172 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38187
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
