# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 455
- HTTP: 126 alive / 96 gold
- HTTPS: 51 alive / 32 gold
- SOCKS4: 173 alive / 158 gold
- SOCKS5: 182 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49323
- Ever gold: 1576

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
