# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 419
- HTTP: 96 alive / 67 gold
- HTTPS: 38 alive / 18 gold
- SOCKS4: 187 alive / 163 gold
- SOCKS5: 195 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48958
- Ever gold: 1569

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
