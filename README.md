# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 384
- HTTP: 100 alive / 53 gold
- HTTPS: 38 alive / 11 gold
- SOCKS4: 175 alive / 155 gold
- SOCKS5: 188 alive / 165 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33426
- Ever gold: 1237

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
