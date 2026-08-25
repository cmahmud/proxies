# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 407
- HTTP: 94 alive / 65 gold
- HTTPS: 76 alive / 20 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 174 alive / 162 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37677
- Ever gold: 1286

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
