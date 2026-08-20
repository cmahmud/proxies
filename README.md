# SyndProxy private pool

## Current pool

- Alive now: 737
- Gold now: 386
- HTTP: 164 alive / 69 gold
- HTTPS: 149 alive / 18 gold
- SOCKS4: 191 alive / 144 gold
- SOCKS5: 233 alive / 155 gold

## Historical pool

- Discovered: 145577
- Ever alive: 25556
- Ever gold: 1064

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
