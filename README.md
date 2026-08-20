# SyndProxy private pool

## Current pool

- Alive now: 1497
- Gold now: 609
- HTTP: 568 alive / 211 gold
- HTTPS: 463 alive / 111 gold
- SOCKS4: 236 alive / 150 gold
- SOCKS5: 230 alive / 137 gold

## Historical pool

- Discovered: 140469
- Ever alive: 23749
- Ever gold: 956

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
